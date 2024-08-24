class Calculatore < Formula
  desc "A simple command-line (Italian) calculator"
  homepage "https://github.com/doribenba/calculatore.git"
  url "https://github.com/doribenba/calculatore/releases/download/v1.0.0/calculatore-1.0.0.tar.gz"
  sha256 "5d966a42516c2fb4b63da3cefd1f7d4100eea671e3f3b0bf22d8f98291aa761c"

  def install
    bin.install "calculatore"
  end

  test do
    system "#{bin}/calculatore", "--help"
  end
end
