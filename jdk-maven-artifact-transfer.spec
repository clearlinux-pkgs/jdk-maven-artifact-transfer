Name     : jdk-maven-artifact-transfer
Version  : 0.9.0
Release  : 1
URL      : http://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-artifact-transfer/0.9.0/maven-artifact-transfer-0.9.0.jar
Source0  : http://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-artifact-transfer/0.9.0/maven-artifact-transfer-0.9.0.jar
Source1  : http://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-artifact-transfer/0.9.0/maven-artifact-transfer-0.9.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-maven-artifact-transfer-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-maven-artifact-transfer package.
Group: Data

%description data
data components for the jdk-maven-artifact-transfer package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/maven-artifact-transfer.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/maven-artifact-transfer.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/maven-artifact-transfer.xml \
%{buildroot}/usr/share/maven-poms/maven-artifact-transfer.pom \
%{buildroot}/usr/share/java/maven-artifact-transfer.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/maven-artifact-transfer.jar
/usr/share/maven-metadata/maven-artifact-transfer.xml
/usr/share/maven-poms/maven-artifact-transfer.pom
